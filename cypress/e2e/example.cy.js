describe('My first test', () => {
  it('checks homepage', () => {
    cy.visit('http://localhost:3000')
    cy.contains('To-Do')
  })
})
