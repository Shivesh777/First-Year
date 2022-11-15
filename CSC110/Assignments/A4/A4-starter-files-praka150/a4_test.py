import a4_part3
import a4_helpers

# print(a4_helpers.rsa_generate_key(89, 97))
# # print(pow(59, 77, 143))
# # print(pow(26, 77, 143))
# # print(pow(40, 77, 143))
# # print(pow(105, 77, 143))
#
# print(a4_part3.rsa_encrypt_block((8633, 7339), 'shivesh is cool'))
# print(a4_part3.rsa_decrypt_block((89, 97, 259), a4_part3.rsa_encrypt_block((8633, 7339), 'shivesh is cool')))
# #print(a4_part3.block_length_generator(8633, 128))




p = int(input("Enter p: "))
q = int(input("Enter q: "))
keys = a4_helpers.rsa_generate_key(p, q)
s = input("Enter message: ")
if len(s) % a4_part3.block_length_generator(p * q, 128) == 0:
    c = a4_part3.rsa_encrypt_block(keys[1], s)
    print(a4_part3.rsa_decrypt_block(keys[0], c) == s)
else:
    print("try again")
