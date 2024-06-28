"use client"

import { Badge } from "../ui/badge";
import { Button, buttonVariants } from "../ui/button";
import useUserStore from "@/context/useUserStore";

interface DishDetailedCardProps {
  id: number;
  name: string;
  description: string;
  price: number;
  img: string;
}

const DishDetailedCard = (dish: DishDetailedCardProps) => {
  
  const addToCart = useUserStore((state) => state.addProduct);
  
  return (
    <div className="card max-w-sm rounded overflow-hidden shadow-lg">
      <img className="w-full object-cover aspect-square" src={dish.img} alt={dish.name} />
      <div className="px-4 py-2 space-y-2">
        <div className="font-bold text-xl mb-2">{dish.name}</div>
        <p className="text-gray-700 text-sm">{dish.description}</p> 
        <Badge className="text-gray-700 text-sm">Price: {dish.price}</Badge>
        <Button className={buttonVariants({
          variant: "outline",
          className: "w-full",
        })}
        onClick={() => addToCart({ 
          id: dish.id, 
          name: dish.name, 
          price: dish.price, 
          quantity: 1
         })}>
          Add to order
        </Button>
      </div>
    </div>
  );
};

export default DishDetailedCard;