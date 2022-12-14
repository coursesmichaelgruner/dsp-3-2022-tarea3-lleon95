#! /bin/octave --persist

pkg load signal

arg_list = argv ();

nroots = str2num(arg_list{1})

num = [1];
den = zeros(1, nroots);
den(1) = 1;
den(nroots) = 1;
zplane(num, den);
