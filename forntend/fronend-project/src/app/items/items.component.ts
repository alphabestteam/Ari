import { Component } from '@angular/core';
import { ItemService } from '../item.service';

@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.scss']
})
export class ItemsComponent {
  items: any[] = [];
  selectedItemId: any;
  showDetails: boolean = false;

  constructor(private itemService: ItemService) { }

  ngOnInit(): void {
    this.fetchItems();
  }

  fetchItems(): void {
    this.itemService.getItems().subscribe(
      (data: any[]) => {
        this.items = data;

      },
      (error) => {
        console.error('Error fetching items:', error);
      }
    );
  }
  
  handleDivClick(item: any): void {
    this.selectedItemId = item.item_id;
    this.showDetails = !this.showDetails;

  }
}
