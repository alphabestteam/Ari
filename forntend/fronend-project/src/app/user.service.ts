// user.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private apiUrl = "http://localhost:8000/api/"; 

  constructor(private http: HttpClient) {}

  // ---------------------------------------------------------      signup      ------------------------------------------------------------------------------------
  registerUser(userData: any): Promise<any> {
    return fetch(`${this.apiUrl}register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    })
  }

  // ---------------------------------------------------------      login      ------------------------------------------------------------------------------------
  loginUser(userData: any): Promise<any> {
    return fetch(`${this.apiUrl}login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
      });
  }
}

