import { Timbre } from './Interface';
import React from 'react';

interface FormProps {
    onAdd: (timbre: Timbre) => void;
  }
  
export const Form: React.FC<FormProps> = ({ onAdd }) => {
    const [datetime, setDatetime] = React.useState('');

    const [message, setMessage] = React.useState('');
   
    const handleSubmit = (event: React.FormEvent) => {
      event.preventDefault();
      const newTimbre: Timbre = {
        datetime: datetime,  // reemplaza con el valor que necesites
        message: message,  // reemplaza con el valor que necesites
    }
    
      onAdd(newTimbre);
      setDatetime('');
      setMessage('');
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <input
          type="datetime-local"
          value={datetime}
          onChange={(event) => setDatetime(event.target.value)}
          required
        />
        <input
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          required
        />
        <button type="submit">Agregar</button>
      </form>
    );
  };
  