import { Component, Input } from '@angular/core';
import { ItemService } from '../item.service';
import { Router } from '@angular/router';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-edit-items',
  templateUrl: './edit-items.component.html',
  styleUrls: ['./edit-items.component.scss']
})
export class EditItemsComponent {
  item:any = {}
  updatedItem: any = {};
  itemId: any

  constructor(private itemService: ItemService,
    private router: Router,
    private route: ActivatedRoute
    ) {}
  
    
    onSubmit() {
      this.route.paramMap.subscribe(params => {
      this.itemId = +params.get('id')!;
      });
      this.updatedItem.id = this.itemId
      this.itemService.updateItems(this.updatedItem.id, this.updatedItem).subscribe(response => {
          console.log(response);
          this.router.navigate(['/personal-area'])
        }, error => {
          console.error('Error updating item:', error);
        });
    }

  }





