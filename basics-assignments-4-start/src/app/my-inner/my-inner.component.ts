import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})

export class MyInnerComponent {
  
  @Input() innerTotal: number = 5;
  @Output() outerTotalChange = new EventEmitter<number>();

  plusClick() {
    this.innerTotal += 1;
    if (this.innerTotal > 10) {
      this.innerTotal = 0;
      this.outerTotalChange.emit(10);
    }
  }

  minusClick() {
    this.innerTotal -= 1;
    if (this.innerTotal < -10) {
      this.innerTotal = 0;
      this.outerTotalChange.emit(-10);
    }
  }
}
