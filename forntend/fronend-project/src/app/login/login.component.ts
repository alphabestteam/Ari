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

  constructor(
    private router: Router,
    private userService: UserService
  ) { }

  onSubmit(): void {
    this.userService.loginUser(this.formData)
      .then(response => {
        console.log(response);
        if (response && response['user_exist']) {
          sessionStorage.setItem('full_name', response['user'].full_name)
          sessionStorage.setItem('user_id', response['user'].user_id)
          sessionStorage.setItem('email', response['user'].email)
          sessionStorage.setItem('admin', response['user'].admin)
          this.goToHome();
               
        } else {
          if(confirm("Don't have an account, want to create a new account?")){
            this.goToSignUp();
          }
        }
      })
      .catch(error => {
        console.error('Login failed', error);
      });
  }

  goToSignUp(): void {
    this.router.navigate(['/signup'])
  }

  goToHome() {
    this.router.navigate(['/welcome'])
  }
}
