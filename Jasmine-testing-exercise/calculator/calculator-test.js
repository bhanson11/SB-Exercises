
it('should calculate the monthly rate correctly', function () {
  const values = {
    amount: 10000,
    years: 10,
    rate: 10
};
expect(calculateMonthlyPayment(values)).toEqual('132.15')
});


it("should return a result with 2 decimal places", function() {
  const values = {
    amount: 10000,
    years: 10,
    rate: 10
  };
  expect(calculateMonthlyPayment(values)).toEqual('132.15');
}); 

/// etc
