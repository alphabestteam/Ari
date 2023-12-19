import { Component } from '@angular/core';
import { ItemService } from '../item.service';
import { Router } from '@angular/router';
import { NgModel } from '@angular/forms';

@Component({
  selector: 'app-upload-items',
  templateUrl: './upload-items.component.html',
  styleUrls: ['./upload-items.component.scss']
})
export class UploadItemsComponent {
  upload: any = {}

  constructor(private itemService: ItemService,
    private router: Router
    ) {}

    onSubmit(): void {
      this.itemService.uploadItems(this.upload)
      .then(response => {
        console.log(response);
        alert("Item added successfully")
        this.goToHome()
      })
      .catch(error => {
        console.error('Upload failed', error);
      });

    }
    goToHome() : void {
      this.router.navigate(['/home'])
    }

}
