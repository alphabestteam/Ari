import { Component } from '@angular/core';
import { UserService } from "../user.service";
import { Router } from '@angular/router';


@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  // styleUrls: ['./sign-up.component.css'],
})
export class SignUpComponent {
  formData: any = {}; 

  constructor(
    private router : Router,
    private userService: UserService
    ) {}

  onSubmit(): void {
    this.userService.registerUser(this.formData)
    this.goToHome()
   
  }
  goToHome() {
    this.router.navigate(['/login'])
  }
}



