import { Component } from '@angular/core';
import { ItemService } from '../item.service';

@Component({
  selector: 'app-edit-items',
  templateUrl: './edit-items.component.html',
  styleUrls: ['./edit-items.component.scss']
})
export class EditItemsComponent {
  item:any = {}

  constructor(private itemService: ItemService) {}
    
    onSubmit(item: any): void {
      console.log(item.item_id);
      const updatedData = { name: 'New Name' };
      this.itemService.updateItems(item.id, updatedData).subscribe(
        (response) => {
          console.log('Item updated successfully', response);
        },
        (error) => {
          console.error('Error updating item', error);
        }
      );
    }
  }

