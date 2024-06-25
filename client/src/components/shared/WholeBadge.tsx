import MaxWidthWrapper from "./MaxWidthWrapper";

const WholeBadge = ({ phrase }: { phrase: string }) => {
  return (
    <div className="bg-primary w-full my-4">
      <MaxWidthWrapper className="py-10">
        <h3 className="text-4xl md:text-6xl font-bold text-center">{phrase}</h3>
      </MaxWidthWrapper>
    </div>
  );
};

export default WholeBadge;
