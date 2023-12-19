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
  myItems: any[]= []

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

  getName(): void {
    this.name = sessionStorage.getItem("full_name")
    this.id = sessionStorage.getItem("user_id")
  }
}
