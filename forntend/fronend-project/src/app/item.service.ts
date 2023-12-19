import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, tap } from 'rxjs';


@Injectable({
  providedIn: 'root'
})

export class ItemService {

  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

// ----------------------------------------    Get Items     ----------------------------------------------------------
  getItems(): Observable<any[]> {
    const url = `${this.apiUrl}items`

    return this.http.get<any[]>(url).pipe(
      catchError(error => {
        console.error('Error fetching items:', error);
        throw error;
      })
    );
  }

// ----------------------------------------   Upload Items    ----------------------------------------------------------
  uploadItems(itemsData: any): Promise<any> {
    return fetch(`${this.apiUrl}items`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(itemsData),
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

// ----------------------------------------   Get Personal Items    ----------------------------------------------------------
getPersonalItems(): Observable<any[]> {
    const id = sessionStorage.getItem("user_id")
    const url = `${this.apiUrl}items/${id}`

    return this.http.get<any[]>(url).pipe(
      catchError(error => {
        console.error('Error fetching items:', error);
        throw error;
      })
    );
  }

}
