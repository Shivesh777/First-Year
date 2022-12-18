# Dependencies: selenium, matplotlib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import matplotlib.pyplot as plt
import csv
from datetime import date
from selenium.webdriver.support.select import Select
from PIL import Image


class BrokeTran:
    def __init__(self, cfg):
        super(BrokeTran, self).__init__()
        self.PATH = cfg.chromedriver
        self.CSV_FILE_PATH = cfg.orbit_params_path
        self.MODTRAN_FOLDER_PATH = cfg.outputs_path

        self.today = date.today()

        self.today_date = self.today.strftime("%b-%d-%Y")

        self.chrome_options = Options()
        if cfg.headless:
            self.chrome_options.add_argument("--headless")

        self.cfg = cfg

    def run(self):

        # PATH = "C:\chromedriver.exe"
        # download location for exe extracted from chromedriver_win32.zip (from https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/)
        # example: "C:\chromedriver.exe"

        # CSV_FILE_PATH = r"C:\Users\dhruv\Downloads\modtran_orbit_params.csv"
        # example: r"C:\Users\user1\Documents\modtran_orbit_params.csv"
        # MODTRAN_FOLDER_PATH = r"C:\Users\dhruv\Documents\Modtran_Graphs"
        # example: r"C:\Users\user1\Documents\Modtran_Graphs"

        self.js_code_snippet = "arguments[0].setAttribute('value', "
        js_code_snippet2 = "arguments[0].setAttribute('style', "

        if False:
            # CSV_FILE_PATH == "uninitialized" or MODTRAN_FOLDER_PATH == "uninitialized" or PATH == "uninitialized":
            print("ERROR: path(s) not initialized")

        else:
            print("Gathering MODTRAN Results...")
            self.driver = webdriver.Chrome(self.PATH, options=self.chrome_options)

            with open(self.CSV_FILE_PATH) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    line_count += 1
                    if line_count > 1:
                        if self.cfg.season == "winter":
                            self.atm_model = 'Mid-Latitude Winter'
                            self.water_column = '1059.7'
                            self.ozone_column = '0.37681'
                            self.ground_temp = '272.15'
                            self.ground_albedo = '0.076'
                        elif self.cfg.season == "spring":
                            self.atm_model = 'US Standard 1976'
                            self.water_column = '1762.3'
                            self.ozone_column = '0.34356'
                            self.ground_temp = '286.82'
                            self.ground_albedo = '0.074'
                        elif self.cfg.season == "summer":
                            self.atm_model = 'Mid-Latitude Summer'
                            self.water_column = '3635.9'
                            self.ozone_column = '0.33176'
                            self.ground_temp = '294.48'
                            self.ground_albedo = '0.084'
                        elif self.cfg.season == "fall":
                            self.atm_model = 'US Standard 1976'
                            self.water_column = '1762.3'
                            self.ozone_column = '0.34356'
                            self.ground_temp = '278.82'
                            self.ground_albedo = '0.090'

                        self.carbon_dioxide = str(self.cfg.carbon_dioxide)
                        self.carbon_monoxide = str(self.cfg.carbon_monoxide)
                        self.methane = str(self.cfg.methane)
                        self.aerosol = self.cfg.aerosol
                        self.visibility = str(self.cfg.visibility)
                        self.sensor_altitude = str(self.cfg.altitude)
                        self.sun_zenith = str(self.cfg.zenith)
                        self.range_lower = str(self.cfg.lambda_min / 1e3)
                        self.range_upper = str(self.cfg.lambda_max / 1e3)
                        self.spectral_res = str(self.cfg.spectral_res / 1e3)

                        self.control("transmittance")
                        spec_res_series, transmittance_series = self.analyze("transmittance")
                        self.control("radiance")
                        _, radiance_series = self.analyze("radiance")

                        return spec_res_series, radiance_series, transmittance_series

    def control(self, mode):
        self.driver.get('http://modtran.spectral.com/modtran_home')

        time.sleep(5)
        self.driver.refresh()

        time.sleep(2)
        if mode == "transmittance":
            btn_mode = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[1]/td[2]/input[1]')
            btn_mode.click()
        elif mode == "radiance":
            btn_mode = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[1]/td[2]/input[2]')
            btn_mode.click()

        # CHANGING ATM Model
        ATM_drop_down = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[3]/td[2]/select')
        select = Select(ATM_drop_down)
        if (self.atm_model == 'Tropical'):
            select.select_by_index(0)
        if (self.atm_model == 'Mid-Latitude Summer'):
            select.select_by_index(1)
        if (self.atm_model == 'Mid-Latitude Winter'):
            select.select_by_index(2)
        if (self.atm_model == 'Sub-Arctic Summer'):
            select.select_by_index(3)
        if (self.atm_model == 'Sub-Arctic Winter'):
            select.select_by_index(4)
        if (self.atm_model == 'US Standard 1976'):
            select.select_by_index(5)

        # CHANGING WC
        WC_text = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[4]/td[2]/input')
        WC_text.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        WC_text.send_keys(self.water_column)

        # CHANGING OC
        OC_text = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[5]/td[2]/input')
        OC_text.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        OC_text.send_keys(self.ozone_column)

        # CHANGING CO2
        CO2_text = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[6]/td[2]/input')
        CO2_text.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        CO2_text.send_keys(self.carbon_dioxide)

        # CHANGING CO
        CO_text = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[7]/td[2]/input')
        CO_text.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        CO_text.send_keys(self.carbon_monoxide)

        # CHANGING CH4
        CH4_text = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[8]/td[2]/input')
        CH4_text.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        CH4_text.send_keys(self.methane)

        # Changing Ground Temperature
        GT_text = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[17]/td[2]/input')
        GT_text.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        GT_text.send_keys(self.ground_temp)

        # CHANGING Ground Albedo
        GA_slider = self.driver.find_element_by_xpath('//*[@id="albedo_slider"]/span')
        move = ActionChains(self.driver)
        offset = round(float(self.ground_albedo) / 0.05)
        move.click_and_hold(GA_slider).move_by_offset(offset, 0).release().perform()

        # CHANGING Aerosol Model
        AM_drop_down = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[21]/td[2]/select')
        select = Select(AM_drop_down)
        if (self.aerosol == 'Rural'):
            print('rural')
            select.select_by_index(0)
        if (self.aerosol == 'Urban'):
            select.select_by_index(1)
        if (self.aerosol == 'Navy Aerosol Model'):
            select.select_by_index(2)
        if (self.aerosol == 'Desert'):
            select.select_by_index(3)

        # CHANGING V
        V_text = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[22]/td[2]/input')
        V_text.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        V_text.send_keys(self.visibility)

        # CHANGING SZ
        sz_drop_down = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[25]/td[2]/select')
        all_children_by_xpath = sz_drop_down.find_elements_by_xpath(".//*")
        js_code_full_sz = self.js_code_snippet + self.sun_zenith + ")"
        self.driver.execute_script(js_code_full_sz, all_children_by_xpath[0])
        select = Select(sz_drop_down)
        select.select_by_index(0)

        # CHANGING SA
        sa_drop_down = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[24]/td[2]/select')
        all_children_by_xpath = sa_drop_down.find_elements_by_xpath(".//*")
        js_code_full_sa = self.js_code_snippet + self.sensor_altitude + ")"
        self.driver.execute_script(js_code_full_sa, all_children_by_xpath[0])
        select = Select(sa_drop_down)
        select.select_by_index(0)

        # Changing SR2
        SR2_slider = self.driver.find_element_by_xpath('//*[@id="spectral_range"]/span[2]')
        move = ActionChains(self.driver)
        # offset = 0.1 * round(float(range_upper)/0.1)
        # offset = round((offset - 0.2)/0.1)
        move.click_and_hold(SR2_slider).move_by_offset(12, 0).release().perform()

        time.sleep(1)

        # Changing SR1
        SR1_slider = self.driver.find_element_by_xpath('//*[@id="spectral_range"]/span[1]')
        move = ActionChains(self.driver)
        # offset = 0.1 * round(float(range_lower)/0.1)
        # offset = round((offset - 0.2)/0.1)
        if self.range_lower == "1.6":
            move.click_and_hold(SR1_slider).move_by_offset(21, 0).release().perform()
        elif self.range_lower == "0.9":
            move.click_and_hold(SR1_slider).move_by_offset(8, 0).release().perform()

        # Changing Res
        if mode == "radiance":
            res_slider = self.driver.find_element_by_xpath('//*[@id="resolution_slider"]/span')
            move = ActionChains(self.driver)
            if self.range_lower == "1.6":
                offset = round(124 - ((0.0085 - float(self.spectral_res)) / (0.0085 - 0.0005) * (124 - (-204))))
            elif self.range_lower == "0.9":
                offset = round(115 - ((0.0087 - float(self.spectral_res)) / (0.0087 - 0.00151) * (115 - (-190))))
            move.click_and_hold(res_slider).move_by_offset(offset, 0).release().perform()
            if float(self.spectral_res) > 0.0085 or float(self.spectral_res) < 0.0005:
                raise NotImplementedError(f"[****] '{self.spectral_res}' is not a valid resolution")

        elif mode == "transmittance":
            res_slider = self.driver.find_element_by_xpath('//*[@id="resolution_slider"]/span')
            move = ActionChains(self.driver)
            if self.range_lower == "1.6":
                offset = round(225 - ((0.0085 - float(self.spectral_res)) / (0.0085 - 0.0005) * (225 - (-102))))
            elif self.range_lower == "0.9":
                offset = round(225 - ((0.0085 - float(self.spectral_res)) / (0.0085 - 0.0005) * (225 - (-101))))
            move.click_and_hold(res_slider).move_by_offset(offset, 0).release().perform()
            if float(self.spectral_res) > 0.0085 or float(self.spectral_res) < 0.0005:
                raise NotImplementedError(f"[****] '{self.spectral_res}' is not a valid resolution")

        # rounded_spec_res = 0.0000233 * round(float(spectral_res)/0.0000233)
        # offset = round((rounded_spec_res - 0.0000339)/0.0000233)
        # pressing submit button
        btn_submit = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/button')
        btn_submit.click()

        time.sleep(5)

    def analyze(self, mode):
        # extracting json data
        div_plot = self.driver.find_element_by_id('plot')
        jsondata = div_plot.get_attribute('innerHTML')

        while (
                jsondata == '<div class="initial_plot_msg"><img src="/static/modtran6/img/spinner.gif"><br>Running MODTRAN...</div>'):
            print("Graph still loading...")
            time.sleep(5)
            jsondata = div_plot.get_attribute('innerHTML')

        # parsing json data
        jsondata = jsondata.split("var docs_json = ")[1].lstrip().split("var render_items")[0].rstrip()

        series = jsondata.split('"data":{"x":')[1].split('},"selected":')[0]

        xseries = series.split(',"y":')[0]
        yseries = series.split(',"y":')[1]

        x_list, y_list = xseries.split(','), yseries.split(',')

        x_list[0], x_list[-1] = x_list[0][1:], x_list[-1][:-1]
        y_list[0], y_list[-1] = y_list[0][1:], y_list[-1][:-1]

        # converting strings in list to floats
        x_float_list, y_float_list = list(map(float, x_list)), list(map(float, y_list))
        if self.cfg.plots_save:
            # plotting
            plt.plot(x_float_list, y_float_list)
            plt.xlabel('Wavelength (Microns)')
            if mode == "transmittance":
                ylabel = 'Transmittance'
            if mode == "radiance":
                ylabel = 'Radiance'
            plt.ylabel(ylabel)
            plt.title("Scenario: " + self.number)

            # saving and closing plot
            title = "\MODTRAN_" + ylabel + "_Scenario_" + self.number + "_" + self.today_date + ".png"
            plt.savefig(self.MODTRAN_FOLDER_PATH + title)
            plt.clf()

        if mode == "radiance":
            # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            WC_text = self.driver.find_element_by_xpath('//*[@id="inputs_table"]/tbody/tr[4]/td[2]/input')
            WC_text.send_keys(Keys.PAGE_DOWN)
            """
            im = Image.open(MODTRAN_FOLDER_PATH + title)
            width, height = im.size
            left = 0
            right = width*.45
            top = height*0.62
            bottom = height
            cropped = im.crop((left, top, right, bottom))
            cropped.save(MODTRAN_FOLDER_PATH + title)
            """
            if self.cfg.plots_save:
                WC_text.send_keys(Keys.PAGE_DOWN)
                title = "\MODTRAN_TOTAL_FLUX_Scenario1_" + self.number + "_" + self.today_date + ".png"
                self.driver.save_screenshot(self.MODTRAN_FOLDER_PATH + title)
                WC_text.send_keys(Keys.PAGE_DOWN)
                title = "\MODTRAN_TOTAL_FLUX_Scenario2_" + self.number + "_" + self.today_date + ".png"
                self.driver.save_screenshot(self.MODTRAN_FOLDER_PATH + title)
                WC_text.send_keys(Keys.PAGE_DOWN)
                title = "\MODTRAN_TOTAL_FLUX_Scenario3_" + self.number + "_" + self.today_date + ".png"
                self.driver.save_screenshot(self.MODTRAN_FOLDER_PATH + title)
                WC_text.send_keys(Keys.PAGE_DOWN)
                title = "\MODTRAN_TOTAL_FLUX_Scenario4_" + self.number + "_" + self.today_date + ".png"
                self.driver.save_screenshot(self.MODTRAN_FOLDER_PATH + title)
                WC_text.send_keys(Keys.PAGE_UP)
                title = "\MODTRAN_TOTAL_FLUX_Scenario5_" + self.number + "_" + self.today_date + ".png"
                self.driver.save_screenshot(self.MODTRAN_FOLDER_PATH + title)
                WC_text.send_keys(Keys.PAGE_UP)
                title = "\MODTRAN_TOTAL_FLUX_Scenario6_" + self.number + "_" + self.today_date + ".png"
                self.driver.save_screenshot(self.MODTRAN_FOLDER_PATH + title)

        return x_float_list, y_float_list
