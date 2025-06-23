import { useState, useEffect } from 'react';
import axios from 'axios';

function JobList() {
  const [jobs, setJobs] = useState([]);
  useEffect(() => {
    axios.get('http://localhost:8000/api/jobs/')
      .then(response => setJobs(response.data))
      .catch(error => console.error('Error fetching jobs:', error));
  }, []);
  return (
    <div className="container mt-5">
      <h1>Jobs</h1>
      <div className="row">
        {jobs.map(job => (
          <div key={job.id} className="col-md-4 mb-3">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{job.title}</h5>
                <p className="card-text">{job.description}</p>
                <p className="card-text"><strong>Budget:</strong> ${job.budget}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
export default JobList;