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

  
  // pay attention the logic here is not correct!!!!!
  onSubmit(): void {

    this.userService.loginUser(this.formData)
      .then(response => {
        console.log(response);
        
        if (response && response['user_exist']) {
          console.log('Login successful, navigating to home');
          sessionStorage.setItem('full_name', response['user'].full_name)
          sessionStorage.setItem('user_id', response['user'].user_id)  
          sessionStorage.setItem('email', response['user'].email)  
          this.goToHome();

        } else {
          alert(response)
          this.goToSignUp();
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
  this.router.navigate(['/home'])
}
}
