import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class UploadService {
  
  private apiUrl = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) { }

// uploadItems(itemsData: any): Promise<any> {
//   return fetch(`${this.apiUrl}items`, {
//   method: 'POST',
//   headers: {
//     'Content-Type': 'application/json',
//   },
//   body: JSON.stringify(itemsData),
// })
// .then(response => {
//   if (!response.ok) {
//     throw new Error('Network response was not ok');
//   }
//   return response.json();
// })
// .catch(error => {
//   console.error('There has been a problem with your fetch operation:', error);
// });

// }
}
