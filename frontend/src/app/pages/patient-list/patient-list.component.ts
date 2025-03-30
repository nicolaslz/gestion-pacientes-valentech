import { Component, OnInit } from '@angular/core';
import { Patient } from '../../models/patient.model';
import { PatientService } from '../../services/patient.service';
import { Subject, debounceTime } from 'rxjs';

@Component({
  selector: 'app-patient-list',
  templateUrl: './patient-list.component.html',
  styleUrls: ['./patient-list.component.scss']
})
export class PatientListComponent implements OnInit {
  patients: Patient[] = [];
  loading: boolean = false;
  nameFilter: string = '';
  diseaseFilter: string = '';
  private searchChanged: Subject<void> = new Subject<void>();

  constructor(private patientService: PatientService) {}
  ngOnInit(): void {
    this.searchChanged.pipe(debounceTime(400)).subscribe(() => {
      this.loadPatients();
    });

    this.loadPatients();
  }
  onSearchChange(): void {
    this.searchChanged.next();
  }

  loadPatients(): void {
    this.loading = true;
    const combinedFilter = (this.nameFilter || this.diseaseFilter)
      ? `${this.nameFilter} ${this.diseaseFilter}`.trim()
      : '';

    this.patientService.getPatients(combinedFilter).subscribe(data => {
      this.patients = data;
      this.loading = false;
    });
  }
}
