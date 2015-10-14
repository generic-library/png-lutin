#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "png file reader and writer"

def get_licence():
	return "png"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "libpng"

def get_maintainer():
	return ["Cosmin Truta"]

def get_version():
	return [1,4,1]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
		'png/png/png.c',
		'png/png/error.c',
		'png/png/get.c',
		'png/png/mem.c',
		'png/png/pread.c',
		'png/png/read.c',
		'png/png/rio.c',
		'png/png/rtran.c',
		'png/png/rutil.c',
		'png/png/set.c',
		'png/png/trans.c',
		'png/png/wio.c',
		'png/png/write.c',
		'png/png/wtran.c',
		'png/png/wutil.c'])
	my_module.compile_flags('c', [
		'-DPNG_NO_LIMITS_H'])
	my_module.compile_version("c", 1999)
	my_module.add_module_depend('z')
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "png"))
	my_module.add_header_file([
		'png/png/config.h',
		'png/png/conf.h',
		'png/png/priv.h',
		'png/png/png.h'
		],
		destination_path="png")
	return my_module


