import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, tap } from 'rxjs';


@Injectable({
  providedIn: 'root'
})

export class ItemService {
  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) {}
  getItems(): Observable<any[]> {
    const url = `${this.apiUrl}items`

    return this.http.get<any[]>(url).pipe(
      catchError(error => {
        console.error('Error fetching items:', error);
        throw error;
    })
    );
  }
}
