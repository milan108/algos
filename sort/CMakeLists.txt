include_directories("${PROJECT_SOURCE_DIR}/utils") 

add_executable (insertion_sort "insertion_sort.c")
add_executable (selection_sort "selection_sort.c")
add_executable (bubble_sort "bubble_sort.c")
add_executable(merge_insertion_sort "merge_insertion_sort.c" )
add_executable(quick_sort "quick_sort.c")
add_library(merge_sort merge_sort.c)

target_link_libraries(merge_insertion_sort utils)
target_link_libraries (bubble_sort utils)
target_link_libraries (insertion_sort utils)
target_link_libraries (selection_sort utils)
target_link_libraries (merge_sort utils)
target_link_libraries (quick_sort utils)

