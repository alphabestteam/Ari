import { Component, OnInit } from '@angular/core';
import { trigger, style, animate, transition } from '@angular/animations';
import { Router } from '@angular/router';


@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.scss'],
  animations: [
    trigger('dropIn', [
      transition(':enter', [
        style({ opacity: 0, transform: 'translateY(-50px)' }),
        animate('1s ease-out', style({ opacity: 1, transform: 'translateY(0)' })),
      ]),
    ]),
  ],

})
export class WelcomeComponent implements OnInit {
  name: any
  constructor(private router: Router,) { }

  ngOnInit(): void {
    this.getName()
  }
  getName(): void {
    this.name = sessionStorage.getItem("full_name")
  }

  goToHome(): void {
    this.router.navigate(['/home'])
  }
}
