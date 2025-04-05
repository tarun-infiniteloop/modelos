// src/main.tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import WorkflowBuilder from './app/page'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <WorkflowBuilder />
  </React.StrictMode>,
)
