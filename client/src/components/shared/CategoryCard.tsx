import Image from "next/image";
import { AspectRatio } from "../ui/aspect-ratio";
import Link from "next/link";

const CategoryCard = ({ name, image, id }: { name: string; image: string, id: number }) => {
  return (
    <Link href={`/menu/${id}`} className="hover:cursor-pointer">
      <AspectRatio ratio={3 / 4}>
        <Image
          src={image}
          alt={name}
          layout="fill"
          objectFit="cover"
          className="rounded-md"
        />
      </AspectRatio>
      <h3 className="text-lg sm:text-xl font-medium">{name}</h3>
    </Link>
  );
};

export default CategoryCard;
