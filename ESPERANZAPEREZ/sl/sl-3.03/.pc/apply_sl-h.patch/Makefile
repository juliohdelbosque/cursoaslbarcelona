#==========================================
#    Makefile: makefile for sl
#	Copyright 1993,1998 Toyoda Masashi 
#		(toyoda@is.titech.ac.jp)
#	Last Modified: 1998/ 7/22
#       Modify for Debian by Hiroyuki Yamamoto <yama1066@gmail.com>
#         2008/12/27
#==========================================

all: sl

sl: sl.c sl.h
	$(CC) $(CFLAGS) -o sl sl.c $(LDFLAGS)

clean::
	rm -f sl

distclean:: clean
