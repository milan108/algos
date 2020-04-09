include_directories("${PROJECT_SOURCE_DIR}/utils")
include_directories("${PROJECT_SOURCE_DIR}/sort")

add_executable(binary_addition "binary_addition.cpp")
add_executable(set_search_sum "set_search_sum.c")
add_executable(polynomials "polynomials.c")

target_link_libraries (polynomials utils)
target_link_libraries (set_search_sum utils)
target_link_libraries (set_search_sum merge_sort)
