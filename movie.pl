:- dynamic (test/6).
:- use_module(library(csv)).
:- csv_read_file("/Users/mymacbookpro/Sites/My-Prolog/movie_all.csv", World, [separator(0',), functor(test)]), forall(member(L, World), assertz(L)).

