# CMakeList.txt : Top-level CMake project file, do global configuration
# and include sub-projects here.
#
cmake_minimum_required (VERSION 3.8)

project ("Algorithms")

# Include sub-projects.
add_subdirectory ("sort")
add_subdirectory ("search")
add_subdirectory("utils")
add_subdirectory("misc")
