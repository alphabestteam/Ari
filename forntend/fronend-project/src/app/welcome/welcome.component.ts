import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.scss']
})

export class WelcomeComponent implements OnInit {
  name: any
  greetingMessage: string = ''
  constructor(private router: Router,) { }
  
  ngOnInit(): void {
  this.getName()
  this.updateGreeting()
  }

  getName(): void {
    this.name = sessionStorage.getItem("full_name")
  }

  goToHome(): void {
    this.router.navigate(['/home'])
  }

  updateGreeting() {
    const currentHour = new Date().getHours();

    if (currentHour >= 0 && currentHour < 12) {
      this.greetingMessage = "Good Morning";
    } else if (currentHour >= 12 && currentHour < 18) {
      this.greetingMessage = "Good Afternoon";
    } else {
      this.greetingMessage = "Good Evening";
    }
  }
}


