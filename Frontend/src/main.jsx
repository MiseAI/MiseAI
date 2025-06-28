import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  createBrowserRouter,
  RouterProvider,
} from 'react-router-dom';

import App from './App.jsx';
import ChatPage from './pages/ChatPage.jsx';
import UploadInvoicePage from './pages/UploadInvoicePage.jsx';

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
  },
  {
    path: '/chat',
    element: <ChatPage />,
  },
  {
    path: '/upload-invoice',
    element: <UploadInvoicePage />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);