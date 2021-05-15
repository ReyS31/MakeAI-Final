import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgxMapboxGLModule } from 'ngx-mapbox-gl';

import { AppComponent } from './app.component';
import { MapComponent } from './components/map/map.component';

@NgModule({
  declarations: [
    AppComponent,
    MapComponent
  ],
  imports: [
    BrowserModule,
    NgxMapboxGLModule.withConfig({
      accessToken: "pk.eyJ1IjoicmVnZXJleW9pIiwiYSI6ImNrM24wejNtaDB4b3IzZHFxazA2bGd4cGkifQ.JwivlB0b6Q9t8WWUlT5MMg",
    }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
