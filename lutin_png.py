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
	return [1,6,21]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'png/png/pngwtran.c',
	    'png/png/pngwrite.c',
	    'png/png/pngpread.c',
	    'png/png/pngrtran.c',
	    'png/png/pngmem.c',
	    'png/png/png.c',
	    'png/png/pngget.c',
	    'png/png/pngwio.c',
	    'png/png/pngtest.c',
	    'png/png/pngtrans.c',
	    'png/png/pngrutil.c',
	    'png/png/pngset.c',
	    'png/png/pngread.c',
	    'png/png/pngrio.c',
	    'png/png/pngwutil.c',
	    'png/png/pngerror.c',
	    ])
	my_module.compile_flags('c', [
	    '-DPNG_NO_LIMITS_H'])
	my_module.compile_version("c", 1999)
	my_module.add_module_depend('z')
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "png"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "generate"))
	my_module.add_header_file([
	    'generate/pnglibconf.h',
	    ],
	    destination_path="png")
	my_module.add_header_file([
	    'png/png/png.h',
	    'png/png/pngpriv.h',
	    'png/png/pngstruct.h',
	    'png/png/pngdebug.h',
	    'png/png/pnginfo.h',
	    'png/png/pngconf.h',
	    ],
	    destination_path="png")
	return my_module


