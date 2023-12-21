import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, tap } from 'rxjs';
import { map } from 'rxjs/operators';



@Injectable({
  providedIn: 'root'
})

export class ItemService {

  private apiUrl = "http://127.0.0.1:8000/api/";
  private items: any[] = [];

  constructor(private http: HttpClient) { }

  // ----------------------------------------    Get Items     ----------------------------------------------------------
  getItems(): Observable<any[]> {
    const url = `${this.apiUrl}items`
    return this.http.get<any[]>(url).pipe(
      tap((items) => {
        this.items = items;
      }),
      catchError(error => {
        console.error('Error fetching items:', error);
        throw error;
      })
    );
  }

  // ----------------------------------------    Get Taken Items     ----------------------------------------------------------
  getTakenItems(): Observable<any[]> {
    return this.getItems().pipe(
      map((items) => {
        const takenItems = items.filter((item) => item.taken);
        return takenItems;
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

  // ----------------------------------------   Delete Item   ----------------------------------------------------------
  deleteItem(id: number): Observable<any> {
    const url = `${this.apiUrl}items/${id}`;
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

  // ----------------------------------------   Update Item   ----------------------------------------------------------
  updateItems(id: number, updatedItem: any): Observable<any> {
    const url = `${this.apiUrl}items/${id}`;
    return this.http.put(url, updatedItem);
  }
}



