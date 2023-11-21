import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  display = false
  counter: number[] = [];
  onClick() {
    this.display = !this.display;
    this.counter.push(this.counter.length + 1);

  }
}
