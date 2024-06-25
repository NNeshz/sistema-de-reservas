const DishCard = ({
  image,
  name,
  description,
}: {
  image: string;
  name: string;
  description: string;
}) => {
  return (
    <div className="col-span-1">
      <div className="relative w-full pb-[177.77%] overflow-hidden">
        {" "}
        <img
          src={image}
          alt={name}
          className="absolute top-0 left-0 w-full h-full object-cover transition-transform duration-300 hover:scale-110 rounded-md"
        />
      </div>
      <div>
        <h3 className="text-xl font-semibold" >{name}</h3>
        <p className="text-sm" >{description}</p>
      </div>
    </div>
  );
};

export default DishCard;
