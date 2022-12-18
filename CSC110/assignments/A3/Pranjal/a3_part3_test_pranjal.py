from hypothesis import given
from hypothesis.strategies import tuples, integers, lists

import a3_part3_pranjal


# @given(
#     vertex_points=lists(tuples(integers(), integers()), min_size=3, max_size=100, unique=True),
#     initial_point=tuples(integers(), integers()),
#     num_points=integers(min_value=1, max_value=1000)
# )
# def test_point_sequence_1(vertex_points: list[tuple[int, int]],
#                           initial_point: tuple[int, int],
#                           num_points: int) -> None:
#     points = a3_part3_pranjal.generate_point_sequence1(vertex_points, initial_point, num_points)
#     assert a3_part3_pranjal.verify_point_sequence1(vertex_points, initial_point, points)


@given(
    vertex_points=lists(tuples(integers(), integers()), min_size=4, max_size=100, unique=True),
    initial_point=tuples(integers(), integers()),
    num_points=integers(min_value=1, max_value=100)
)
def test_point_sequence_2(vertex_points: list[tuple[int, int]],
                          initial_point: tuple[int, int],
                          num_points: int) -> None:
    points = a3_part3_pranjal.generate_point_sequence2(vertex_points, initial_point, num_points)
    assert a3_part3_pranjal.verify_point_sequence2(vertex_points, initial_point, points)
