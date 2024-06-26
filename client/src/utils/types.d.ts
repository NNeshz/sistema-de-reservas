export interface CategoryItem {
  id: number;
  name: string;
  img: string;
}

export interface Categories {
  [key: string]: CategoryItem[];
}
