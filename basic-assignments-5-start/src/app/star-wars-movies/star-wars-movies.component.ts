import { Component, OnInit } from '@angular/core';
import { FILMS } from '../star-wars-fake-db/film-data';
import { ActivatedRoute, Router } from '@angular/router';
import { StarWarsMovie } from '../interface';

@Component({
  selector: 'app-star-wars-movies',
  templateUrl: './star-wars-movies.component.html',
  styleUrls: ['./star-wars-movies.component.scss'],
})

export class StarWarsMoviesComponent implements OnInit {
  movies: StarWarsMovie[] = [];

  constructor(private route: ActivatedRoute, private router: Router) {}

  ngOnInit(){
    this.movies = FILMS;
  }
}







