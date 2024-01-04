import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <input type="checkbox" id="1" name="1" [(ngModel)]="items[0].checked">
    <label for="1">A</label><br>

    <input type="checkbox" id="2" name="2" [(ngModel)]="items[1].checked"> 
    <label for="2">B</label><br>

    <input type="checkbox" id="3" name="3" [(ngModel)]="items[2].checked">
    <label for="3">C</label><br>

    <button (click)="addToCart()">Add to your cart</button>
  `,
})
export class AppComponent {
  items = [
    { id: 1, name: 'A', checked: false },
    { id: 2, name: 'B', checked: false },
    { id: 3, name: 'C', checked: false },
  ];

  addToCart() {
    const newItems = this.items.filter(item => item.checked);

    // create an array of names based on newItems array
    this.cartItems.push(...newItems.map(item => item.name));

    localStorage.setItem('cartItems', JSON.stringify(this.cartItems));
    if (newItems.length == 0) {
      alert("You have to chose at least one item")
    } else {
      alert(`Items added to your cart! and now your cart's amount is: ${this.cartItems.length}`);
  
    }
  }
  cartItems: string[] = (JSON.parse(localStorage.getItem('cartItems')!) as string[]) || [];
}
