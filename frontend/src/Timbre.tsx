import { TimbreListProps } from './Interface';

export const TimbreList: React.FC<TimbreListProps> = ({ timbres }) => (
    <ul>
      {timbres.map((timbre, index) => (
        <li key={index}>
          {timbre.datetime}
          {timbre.message}
        </li>
      ))}
    </ul>
  );
  