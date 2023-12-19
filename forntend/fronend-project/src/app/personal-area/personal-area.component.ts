import { Component } from '@angular/core';
import { ItemService } from '../item.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-personal-area',
  templateUrl: './personal-area.component.html',
  styleUrls: ['./personal-area.component.scss']
})
export class PersonalAreaComponent {
  name: any
  id : any
  myItems: any[] = []

  clickedItem: boolean = false;

  ngOnInit(): void {
    this.getName()
    this.fetchPersonalItems()
  }

  constructor(private itemService: ItemService,
    private router: Router
  ) { }

  fetchPersonalItems(): void {
    this.itemService.getPersonalItems().subscribe(
      (data: any[]) => {
        this.myItems = data.map(item => ({ ...item, clicked: false }));
      },

      (error) => {
        console.error('Error fetching items:', error);
      }
    );
  }

  handleDivClick(item: any): void {
    console.log(item)
  }

  getName(): void {
    this.name = sessionStorage.getItem("full_name")
    this.id = sessionStorage.getItem("user_id")
  }

  onDelete(item: any): void {
    console.log(item.id);
    this.itemService.deleteItem(item.id).subscribe(
      () => {
        console.log('Item deleted successfully');
      },
      (error) => {
        console.log(item.uploaded_by)
        console.error('Error deleting item', error);
      }
    );
  }
  onclick(): void {
    this.router.navigate(['/editItems'])

  }
}

