import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { ItemService } from './item.service';
import { FileUploadModule } from 'ng2-file-upload';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { HttpClientModule } from '@angular/common/http';
import { SignUpComponent } from './sign-up/sign-up.component';
import { HomeComponent } from './home/home.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { ItemsComponent } from './items/items.component';
import { UploadItemsComponent } from './upload-items/upload-items.component';
import { TakenItemsComponent } from './taken-items/taken-items.component';
import { PersonalAreaComponent } from './personal-area/personal-area.component';
import { EditItemsComponent } from './edit-items/edit-items.component';
import { AboutComponent } from './about/about.component';
import { WelcomeComponent } from './welcome/welcome.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignUpComponent,
    HomeComponent,
    NavbarComponent,
    FooterComponent,
    ItemsComponent,
    UploadItemsComponent,
    TakenItemsComponent,
    PersonalAreaComponent,
    EditItemsComponent,
    AboutComponent,
    WelcomeComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    FileUploadModule,
    BrowserAnimationsModule
  ],
  providers: [ItemService],
  bootstrap: [AppComponent]
})
export class AppModule { }
