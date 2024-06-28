export interface CategoryItem {
  id: number;
  name: string;
  img: string;
}

export interface Categories {
  [key: string]: CategoryItem[];
}

export interface LoginUserForm {
  username: string;
  password: string;
}

export interface RegisterUserForm {
  username: string;
  password: string;
}

export interface ProductItem {
  id: number;
  name: string;
  price: number;
  quantity: number;
}

export interface CartStore {
  products: ProductItem[];

  addProduct: (product: ProductItem) => void;
  removeProduct: (productId: number) => void;
}