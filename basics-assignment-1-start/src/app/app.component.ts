import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  isSuccess: boolean = true;
  onClick() {
    this.isSuccess = !this.isSuccess
    this.changeText()
  }

  clicked: boolean = false;
  btnText = "Button";

  changeText() {
    if (this.clicked) {
      this.btnText = "Show warning alert!"
      this.clicked = !this.clicked
    } else {
      this.btnText = "Show success alert!"
      this.clicked = !this.clicked
    }
  }
}

