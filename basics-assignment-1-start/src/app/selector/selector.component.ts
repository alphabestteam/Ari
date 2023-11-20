import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-selector',
  templateUrl: './selector.component.html',
  styleUrl: './selector.component.css'
})

export class SelectorComponent {
  selectedAlert: boolean = true;
  repeatCount: number = 0;
  readonly repeatOptions: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  isSuccess: boolean = true;
  changeAlerts(): void {
    this.selectedAlert = !this.selectedAlert;
  }

  getRepeatArray(): number[] {
    const repeatArray: number[] = Array.from({ length: this.repeatCount }, (_, i) => i + 1);
    return repeatArray;
  }
}
