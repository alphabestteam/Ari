import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError } from 'rxjs';
import { response } from 'express';

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

// ---------------------------------------------------------      Admin get all users      ------------------------------------------------------------------------------------
getAllUsers(): Promise<any> {
  return fetch(`${this.apiUrl}register`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .catch(error => {
      console.error('There has been a problem with your fetch operation:', error);
      throw error;
    });
  }

// ---------------------------------------------------------      Admin Delete users      ------------------------------------------------------------------------------------
deleteUSers(id: number): Observable<any> {
  const url = `${this.apiUrl}users/${id}`;

  return new Observable(observer => {
    fetch(url, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        observer.next(data);
        observer.complete();
      })
      .catch(error => {
        observer.error(error);
        observer.complete();
      });
  });
}
}


