import { Component } from '@angular/core';
import { ItemService } from '../item.service';
import { Router } from '@angular/router';
import { UserService } from '../user.service';

@Component({
  selector: 'app-personal-area',
  templateUrl: './personal-area.component.html',
  styleUrls: ['./personal-area.component.scss']
})
export class PersonalAreaComponent {
  name: any
  id: any
  admin: any

  myItems: any[] = []
  items: any[] = []
  users: any[] = []


  clickedItem: boolean = false;

  ngOnInit(): void {
    this.getName()
    this.fetchPersonalItems()
    this.fetchItems()
    this.getAllUsers()
  }

  constructor(private itemService: ItemService,
    private userService: UserService,
    private router: Router
  ) { }

  getAllUsers(): void {
    this.userService.getAllUsers().then(
      (data: any) => {
        this.users = data;
      }
    )
      .catch(error => {
        console.error('Error fetching users:', error);
      });
  }
  
  fetchItems(): void {
    this.itemService.getItems().subscribe(
      (data: any[]) => {
        this.items = data.map(item => ({ ...item, clicked: false }));
      },
      (error) => {
        console.error('Error fetching items:', error);
      }
    );
  }

  
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
    this.admin = sessionStorage.getItem("admin")
  }

  onDelete(itemId: any): void {
  
    this.itemService.deleteItem(itemId).subscribe(
      () => {
        console.log('Item deleted successfully');
        this.fetchPersonalItems()
      },
      (error) => {
        console.error('Error deleting item', error);
      }
    );
  }

  adminOnDelete(itemId: any): void {
    this.itemService.deleteItem(itemId).subscribe(
      () => {
        console.log('Item deleted successfully');
        this.fetchItems()
      },
      (error) => {
        console.error('Error deleting item', error);
      }
    );
  }

  onclick(itemId: any, itemName: any, city:any): void {
    this.router.navigate(['/editItems', itemId, itemName, city])
  }

  onDeleteUser(user: any): void {
    this.userService.deleteUSers(user.id).subscribe(
      () => {
        console.log('User deleted successfully');
        this.getAllUsers()
      },
      (error) => {
        console.error('Error user item', error);
      }
    );
  }
}


