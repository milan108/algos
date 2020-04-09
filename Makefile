# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/milan/practice/algos

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/milan/practice/algos

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
	/usr/bin/cmake --regenerate-during-build -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake cache editor..."
	/usr/bin/ccmake -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start /home/milan/practice/algos/CMakeFiles /home/milan/practice/algos/CMakeFiles/progress.marks
	$(MAKE) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start /home/milan/practice/algos/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named selection_sort

# Build rule for target.
selection_sort: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 selection_sort
.PHONY : selection_sort

# fast build rule for target.
selection_sort/fast:
	$(MAKE) -f sort/CMakeFiles/selection_sort.dir/build.make sort/CMakeFiles/selection_sort.dir/build
.PHONY : selection_sort/fast

#=============================================================================
# Target rules for targets named merge_sort

# Build rule for target.
merge_sort: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 merge_sort
.PHONY : merge_sort

# fast build rule for target.
merge_sort/fast:
	$(MAKE) -f sort/CMakeFiles/merge_sort.dir/build.make sort/CMakeFiles/merge_sort.dir/build
.PHONY : merge_sort/fast

#=============================================================================
# Target rules for targets named quick_sort

# Build rule for target.
quick_sort: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 quick_sort
.PHONY : quick_sort

# fast build rule for target.
quick_sort/fast:
	$(MAKE) -f sort/CMakeFiles/quick_sort.dir/build.make sort/CMakeFiles/quick_sort.dir/build
.PHONY : quick_sort/fast

#=============================================================================
# Target rules for targets named insertion_sort

# Build rule for target.
insertion_sort: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 insertion_sort
.PHONY : insertion_sort

# fast build rule for target.
insertion_sort/fast:
	$(MAKE) -f sort/CMakeFiles/insertion_sort.dir/build.make sort/CMakeFiles/insertion_sort.dir/build
.PHONY : insertion_sort/fast

#=============================================================================
# Target rules for targets named bubble_sort

# Build rule for target.
bubble_sort: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 bubble_sort
.PHONY : bubble_sort

# fast build rule for target.
bubble_sort/fast:
	$(MAKE) -f sort/CMakeFiles/bubble_sort.dir/build.make sort/CMakeFiles/bubble_sort.dir/build
.PHONY : bubble_sort/fast

#=============================================================================
# Target rules for targets named merge_insertion_sort

# Build rule for target.
merge_insertion_sort: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 merge_insertion_sort
.PHONY : merge_insertion_sort

# fast build rule for target.
merge_insertion_sort/fast:
	$(MAKE) -f sort/CMakeFiles/merge_insertion_sort.dir/build.make sort/CMakeFiles/merge_insertion_sort.dir/build
.PHONY : merge_insertion_sort/fast

#=============================================================================
# Target rules for targets named linear_search

# Build rule for target.
linear_search: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 linear_search
.PHONY : linear_search

# fast build rule for target.
linear_search/fast:
	$(MAKE) -f search/CMakeFiles/linear_search.dir/build.make search/CMakeFiles/linear_search.dir/build
.PHONY : linear_search/fast

#=============================================================================
# Target rules for targets named binary_search

# Build rule for target.
binary_search: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 binary_search
.PHONY : binary_search

# fast build rule for target.
binary_search/fast:
	$(MAKE) -f search/CMakeFiles/binary_search.dir/build.make search/CMakeFiles/binary_search.dir/build
.PHONY : binary_search/fast

#=============================================================================
# Target rules for targets named utils

# Build rule for target.
utils: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 utils
.PHONY : utils

# fast build rule for target.
utils/fast:
	$(MAKE) -f utils/CMakeFiles/utils.dir/build.make utils/CMakeFiles/utils.dir/build
.PHONY : utils/fast

#=============================================================================
# Target rules for targets named polynomials

# Build rule for target.
polynomials: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 polynomials
.PHONY : polynomials

# fast build rule for target.
polynomials/fast:
	$(MAKE) -f misc/CMakeFiles/polynomials.dir/build.make misc/CMakeFiles/polynomials.dir/build
.PHONY : polynomials/fast

#=============================================================================
# Target rules for targets named binary_addition

# Build rule for target.
binary_addition: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 binary_addition
.PHONY : binary_addition

# fast build rule for target.
binary_addition/fast:
	$(MAKE) -f misc/CMakeFiles/binary_addition.dir/build.make misc/CMakeFiles/binary_addition.dir/build
.PHONY : binary_addition/fast

#=============================================================================
# Target rules for targets named set_search_sum

# Build rule for target.
set_search_sum: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 set_search_sum
.PHONY : set_search_sum

# fast build rule for target.
set_search_sum/fast:
	$(MAKE) -f misc/CMakeFiles/set_search_sum.dir/build.make misc/CMakeFiles/set_search_sum.dir/build
.PHONY : set_search_sum/fast

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... edit_cache"
	@echo "... rebuild_cache"
	@echo "... binary_addition"
	@echo "... binary_search"
	@echo "... bubble_sort"
	@echo "... insertion_sort"
	@echo "... linear_search"
	@echo "... merge_insertion_sort"
	@echo "... merge_sort"
	@echo "... polynomials"
	@echo "... quick_sort"
	@echo "... selection_sort"
	@echo "... set_search_sum"
	@echo "... utils"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system

