export interface Timbre {
    datetime: string
    message: string
  }
  
export interface TimbreListProps {
    timbres: Timbre[];
}

export interface TimbreProps {
    timbre: Timbre;
  }