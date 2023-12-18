import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from "../user.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})

export class LoginComponent {

  formData: any = {}

  constructor (
    private router: Router,
    private userService : UserService
  ) {}

  onSubmit(): void {
    this.userService.loginUser(this.formData)
      .then(response => {
      console.log(response)
      alert(response)
    })
    .catch(error => {
      console.error('login failed', error);
    });
  }

goToSignUp(): void {
  this.router.navigate(['/signup'])
}

goToHome() {
  this.router.navigate(['/home'])
}
}
