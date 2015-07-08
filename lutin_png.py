#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "png file reader and writer"

def create(target):
	myModule = module.Module(__file__, 'png', 'LIBRARY')
	myModule.add_src_file([
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
	myModule.compile_flags('c', [
		'-DPNG_NO_LIMITS_H'])
	myModule.compile_version_CC(1999)
	myModule.add_module_depend('z')
	myModule.add_export_path(tools.get_current_path(__file__) + "/png")
	return myModule


